import evergreen
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    evergreen.button(
        id='input',
        value='my-value',
        label='my-label',
        size="large",
        isActive=True,
        # intent="danger",
        children='a brand new button!'
    ),
    html.Div(id='output')
])


@app.callback(Output('output', 'children'), [Input('input', 'n_clicks')])
def display_output(value):
    if value is None:
        return "You have not clicked this button."
    else:
        return 'You have clicked this button {} times'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
