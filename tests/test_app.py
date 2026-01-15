import pytest
import pandas as pd
from dash import html, dcc
from pathlib import Path

from pink_morsels.web import create_app
from pink_morsels.data import load_data, daily_sales_by_region
from pink_morsels.viz import make_figure


def find_component_by_id(tree, id_value):
    # recursive search for component with matching id
    comp_id = getattr(tree, 'id', None)
    if comp_id == id_value:
        return tree
    # dash components sometimes store props in .props; also support .children attr
    props = getattr(tree, 'props', None)
    children = None
    if props is not None:
        children = props.get('children')
    else:
        children = getattr(tree, 'children', None)

    if children is None:
        return None
    if isinstance(children, (list, tuple)):
        for c in children:
            res = find_component_by_id(c, id_value)
            if res is not None:
                return res
    else:
        return find_component_by_id(children, id_value)
    return None


def find_component_by_type(tree, comp_type):
    # match based on class or by tag name fallback
    if hasattr(tree, '__class__') and tree.__class__ is comp_type:
        return tree

    # check children as above
    props = getattr(tree, 'props', None)
    children = None
    if props is not None:
        children = props.get('children')
    else:
        children = getattr(tree, 'children', None)

    if children is None:
        return None
    if isinstance(children, (list, tuple)):
        for c in children:
            res = find_component_by_type(c, comp_type)
            if res is not None:
                return res
    else:
        return find_component_by_type(children, comp_type)
    return None


@pytest.fixture
def dash_app():
    return create_app()


def test_header_present(dash_app):
    layout = dash_app.layout
    h1 = find_component_by_type(layout, html.H1)
    assert h1 is not None
    children = getattr(h1, 'props', {}).get('children', getattr(h1, 'children', ''))
    assert 'Pink Morsels' in children


def test_visualisation_present(dash_app):
    layout = dash_app.layout
    graph = find_component_by_id(layout, 'sales-graph')
    assert graph is not None
    assert isinstance(graph, dcc.Graph)


def test_region_picker_present(dash_app):
    layout = dash_app.layout
    picker = find_component_by_id(layout, 'region-picker')
    assert picker is not None
    assert isinstance(picker, dcc.RadioItems)


def test_load_data():
    df = load_data()
    assert not df.empty
    assert 'Date' in df.columns
    assert 'Sales' in df.columns
    assert 'Region' in df.columns
    assert pd.api.types.is_datetime64_any_dtype(df['Date'])


def test_daily_sales_all_regions():
    df = load_data()
    result = daily_sales_by_region(df, 'all')
    assert not result.empty
    assert 'Date' in result.columns
    assert 'Sales' in result.columns
    assert result['Sales'].sum() > 0


def test_daily_sales_specific_region():
    df = load_data()
    result = daily_sales_by_region(df, 'north')
    assert not result.empty
    assert result['Sales'].sum() > 0
    all_result = daily_sales_by_region(df, 'all')
    assert result['Sales'].sum() < all_result['Sales'].sum()


def test_make_figure():
    df = load_data()
    daily = daily_sales_by_region(df, 'all')
    fig = make_figure(daily)
    assert fig is not None
    assert 'data' in fig
    assert len(fig['data']) > 0


def test_region_picker_options(dash_app):
    layout = dash_app.layout
    picker = find_component_by_id(layout, 'region-picker')
    options = picker.options
    assert len(options) == 5
    values = [opt['value'] for opt in options]
    assert 'all' in values
    assert 'north' in values
    assert 'east' in values
    assert 'south' in values
    assert 'west' in values
