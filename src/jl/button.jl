# AUTO GENERATED FILE - DO NOT EDIT

export button

"""
    button(;kwargs...)
    button(children::Any;kwargs...)
    button(children_maker::Function;kwargs...)


A button component.

Keyword arguments:
- `children` (String; optional)
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `appearance` (String; optional)
- `className` (String; optional)
- `disabled` (Bool; optional)
- `iconAfter` (dash component; optional)
- `iconBefore` (dash component; optional)
- `intent` (String; optional)
- `isActive` (Bool; optional)
- `isLoading` (Bool; optional)
- `label` (String; required): A label that will be printed when this component is rendered.
- `n_clicks` (Real; optional)
- `size` (a value equal to: "small", "medium", "large"; optional): Dash-assigned callback that should be called to report property changes
to Dash, to make them available for callbacks.
- `value` (String; optional): The value displayed in the input.
"""
function button(; kwargs...)
        available_props = Symbol[:children, :id, :appearance, :className, :disabled, :iconAfter, :iconBefore, :intent, :isActive, :isLoading, :label, :n_clicks, :size, :value]
        wild_props = Symbol[]
        return Component("button", "button", "evergreen", available_props, wild_props; kwargs...)
end

button(children::Any; kwargs...) = button(;kwargs..., children = children)
button(children_maker::Function; kwargs...) = button(children_maker(); kwargs...)

