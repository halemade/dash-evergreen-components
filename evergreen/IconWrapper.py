# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class IconWrapper(Component):
    """An IconWrapper component.
This is an internal helper component for rendering custom or Evergreen icons
Box props are applied to the outer Box container, and Evergreen icon-specific props are added to the icon element.

Keyword arguments:

- color (string; optional):
    Color of icon. Equivalent to setting CSS `fill` property.

- icon (dash component; optional):
    The icon component - whether an Evergreen icon or a custom icon
    node:  - If `None` or `undefined` or `False`, this component will
    render nothing. - If given a `JSX.Element`, that element will be
    rendered, with size/color/title props cloned into it - If given a
    React element type, it will be rendered with the other icon props
    As a consumer, you should never use `<IconWrapper icon={<element
    />}` directly; simply render `<element />` instead.

- size (number; optional):
    Size of the icon, in pixels. Icons contains 16px and 20px SVG icon
    paths, and chooses the appropriate resolution based on this prop.

- title (string; optional):
    Description string. Browsers usually render this as a tooltip on
    hover, whereas screen readers will use it for aural feedback. By
    default, this is set to the icon's name for accessibility."""
    @_explicitize_args
    def __init__(self, color=Component.UNDEFINED, icon=Component.UNDEFINED, size=Component.UNDEFINED, title=Component.UNDEFINED, **kwargs):
        self._prop_names = ['color', 'icon', 'size', 'title']
        self._type = 'IconWrapper'
        self._namespace = 'evergreen'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['color', 'icon', 'size', 'title']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(IconWrapper, self).__init__(**args)
