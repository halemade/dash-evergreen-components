# AUTO GENERATED FILE - DO NOT EDIT

#' @export
iconWrapper <- function(color=NULL, icon=NULL, size=NULL, title=NULL) {
    
    props <- list(color=color, icon=icon, size=size, title=title)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'IconWrapper',
        namespace = 'evergreen',
        propNames = c('color', 'icon', 'size', 'title'),
        package = 'evergreen'
        )

    structure(component, class = c('dash_component', 'list'))
}
