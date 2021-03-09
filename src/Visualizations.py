import pandas as pd
import altair as alt
import numpy as np
from altair import datum

from src import wrangling as wr

alt.data_transformers.disable_max_rows()
alt.themes.enable('latimes')

gdp = wr.gdp


def plt_total_gdp(year, Geography):
    bar = alt.Chart(gdp, title="Total GDP ").mark_bar(size=80).transform_aggregate(
        groupby=['Geography', 'Year'], GDP='sum(GDP)').encode(
        x=alt.X('sum(GDP):Q', title='GDP (dollars x 1,000,000)',
                axis=alt.Axis(grid=False, ticks=False, labels=False, labelFontSize=10)),
        y=alt.Y('Geography:O', sort='-x', title=None, axis=alt.Axis(grid=False, labelFontSize=20)),
        tooltip=[alt.Tooltip('sum(GDP):Q', format=('$,.2f'), title='Total GDP $')]).transform_filter(
        alt.FieldEqualPredicate(field='Geography', equal=Geography)).transform_filter(
        alt.FieldEqualPredicate(field='Year', equal=year)).properties(height=200, width=400)

    total_gdp = bar.mark_text(dx=-175, color='darkblue', size=60).encode(
        text=alt.Text('sum(GDP):Q', format='$,.2f')).configure_view(strokeOpacity=0)

    return total_gdp.to_html()


def plt_historical_gdp(year, Geography):
    historical_gdp = alt.Chart(gdp, title="GDP Historical Evolution").mark_line(
        point=alt.OverlayMarkDef(filled=False, fill='darkblue'), size=5).encode(
        x=alt.X('Year', axis=alt.Axis(grid=False, ticks=False, format='Y', labelFontSize=10), title='Year'),
        y=alt.Y('sum(GDP):Q', axis=alt.Axis(grid=False, ticks=False, format='$,f', labelFontSize=10),
                title='GDP (dollars x 1,000,000)'),
        tooltip=[alt.Tooltip('Year'),
                 alt.Tooltip('sum(GDP):Q', format='$,.2f', title='Total GDP $')]).transform_filter(
        alt.FieldEqualPredicate(field='Geography', equal=Geography)).transform_filter(
        alt.FieldRangePredicate('Year', [1997, year])).configure_view(strokeOpacity=0).properties(height=200, width=400)

    return historical_gdp.to_html()


def plt_indus_contri(year, Geography):
    industry_gdp = alt.Chart(gdp, title="GDP Industry Contribution").mark_bar().encode(
        x=alt.X('sum(GDP):Q', title='GDP (dollars x 1,000,000)', axis=alt.Axis(format='$,f', labelFontSize=10)),
        y=alt.Y('Industry:O', sort='-x'),
        color=alt.Color('sum(GDP)', title='Total GDP', scale=alt.Scale(scheme='lighttealblue')),
        tooltip=[alt.Tooltip('Industry'),
                 alt.Tooltip('sum(GDP):Q', format=('$,.2f'), title='Total GDP $')]).transform_filter(
        alt.FieldEqualPredicate(field='Geography', equal=Geography)).transform_filter(
        alt.FieldEqualPredicate(field='Year', equal=year)).configure_view(strokeOpacity=0)

    return industry_gdp.to_html()


def plt_province_gdp(year):
    industry_gdp = alt.Chart(gdp, title="GDP Industry Contribution").mark_bar().encode(
        x=alt.X('sum(GDP):Q', title='GDP (dollars x 1,000,000)', axis=alt.Axis(format='$,f', labelFontSize=10)),
        y=alt.Y('Industry:O', sort='-x'),
        color=alt.Color('sum(GDP)', title='Total GDP', scale=alt.Scale(scheme='lighttealblue')),
        tooltip=[alt.Tooltip('Industry'),
                 alt.Tooltip('sum(GDP):Q', format='$,.2f', title='Total GDP $')]).transform_filter(
        alt.FieldEqualPredicate(field='Geography', equal=Geography)).transform_filter(
        alt.FieldEqualPredicate(field='Year', equal=year)).configure_view(strokeOpacity=0)
    return industry_gdp


# test
if __name__ == '__main__':
    year = 2010
    Geography = 'Ontario'

    chart = plt_province_gdp(year)
    chart.show()
