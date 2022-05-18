import altair as alt
from altair import expr, datum

def funnel_chart(df: pd.DataFrame, step_column: str = "step", count_column: str = "count", width: int = 800, height: int = 400):
    # Конверсия шага
    df["cr"] = 1 + df[count_column].pct_change()
    df["cr_diff"] = df[count_column].pct_change()

    base = alt.Chart(df)\
        .transform_calculate(
            # Конверсия к начальному этапу
            cr0 = f"datum.{count_column} / {df.loc[0, count_column]}"
        )\
        .encode(
        x = alt.X(f"{count_column}:Q", stack="center", sort="ascending", title = "", axis=None),
        y = alt.Y(f"{step_column}", sort=None, title=""),
        tooltip = [
                    alt.Tooltip(f"{step_column}", title="Этап"), 
                    alt.Tooltip(f"{count_column}", title="Количество:"),
                    alt.Tooltip("cr0:Q", title="Доля от начального этапа", format=".1%"),
                    alt.Tooltip("cr:Q", title="Доля от предыдущего этапа", format=".1%"),
                    alt.Tooltip("cr_diff", title="Изменение", format=".1%")
                ]
    )

    funnel = base.mark_bar().encode(color = alt.Color(f"{step_column}", legend=None))
    text = base.mark_text(dx = 20).encode(text = "count")
    
    plot = (funnel + text).properties(
        width = width,
        height = height
    )
    
    df = df.drop(columns=["cr", "cr_diff"])
    
    return plot
