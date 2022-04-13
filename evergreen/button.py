# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class button(Component):
    """A button component.


Keyword arguments:

- children (string; optional):
    The number of clicks the button has recieved this sesson.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- appearance (string; default "default"):
    One of \"none\", \"success\", or \"danger\". The default is none.

- className (string; optional):
    When True, the button is disabled. isLoading also sets the button
    to disabled.

- disabled (boolean; optional):
    Sets an icon after the text. Can be any icon from Evergreen or a
    custom element.

- iconAfter (dash component; optional):
    Sets an icon before the text. Can be any icon from Evergreen or a
    custom element.

- iconBefore (dash component; default False):
    A label that will be printed when this component is rendered.

- intent (string; default "none"):
    The size of the button.

- isActive (boolean; default True):
    if True, this will show a loading indicator and disable the
    button.

- isLoading (boolean; default False):
    The evergreen appearance property, \"default\", \"primary\", or
    \"minimal\".

- label (string; default ''):
    A label that will be printed when this component is rendered.

- n_clicks (number; default 0):
    Class name passed to the button.

- size (a value equal to: "small", "medium", "large"; default 'medium'):
    Dash-assigned callback that should be called to report property
    changes to Dash, to make them available for callbacks.

- value (string; optional):
    The value displayed in the input."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, label=Component.UNDEFINED, value=Component.UNDEFINED, size=Component.UNDEFINED, intent=Component.UNDEFINED, appearance=Component.UNDEFINED, isLoading=Component.UNDEFINED, isActive=Component.UNDEFINED, iconBefore=Component.UNDEFINED, iconAfter=Component.UNDEFINED, disabled=Component.UNDEFINED, className=Component.UNDEFINED, n_clicks=Component.UNDEFINED, onClick=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'appearance', 'className', 'disabled', 'iconAfter', 'iconBefore', 'intent', 'isActive', 'isLoading', 'label', 'n_clicks', 'size', 'value']
        self._type = 'button'
        self._namespace = 'evergreen'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'appearance', 'className', 'disabled', 'iconAfter', 'iconBefore', 'intent', 'isActive', 'isLoading', 'label', 'n_clicks', 'size', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(button, self).__init__(children=children, **args)
