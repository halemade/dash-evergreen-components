# AUTO GENERATED FILE - DO NOT EDIT

#' @export
button <- function(children=NULL, id=NULL, appearance=NULL, className=NULL, disabled=NULL, iconAfter=NULL, iconBefore=NULL, intent=NULL, isActive=NULL, isLoading=NULL, label=NULL, n_clicks=NULL, size=NULL, value=NULL) {
    
    props <- list(children=children, id=id, appearance=appearance, className=className, disabled=disabled, iconAfter=iconAfter, iconBefore=iconBefore, intent=intent, isActive=isActive, isLoading=isLoading, label=label, n_clicks=n_clicks, size=size, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'button',
        namespace = 'evergreen',
        propNames = c('children', 'id', 'appearance', 'className', 'disabled', 'iconAfter', 'iconBefore', 'intent', 'isActive', 'isLoading', 'label', 'n_clicks', 'size', 'value'),
        package = 'evergreen'
        )

    structure(component, class = c('dash_component', 'list'))
}
