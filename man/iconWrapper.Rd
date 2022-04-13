% Auto-generated: do not edit by hand
\name{iconWrapper}

\alias{iconWrapper}

\title{IconWrapper component}

\description{
This is an internal helper component for rendering custom or Evergreen icons Box props are applied to the outer Box container, and Evergreen icon-specific props are added to the icon element.
}

\usage{
iconWrapper(color=NULL, icon=NULL, size=NULL, title=NULL)
}

\arguments{
\item{color}{Character. Color of icon. Equivalent to setting CSS `fill` property.}

\item{icon}{Dash component. The icon component - whether an Evergreen icon or a custom icon node:

- If `null` or `undefined` or `false`, this component will render nothing.
- If given a `JSX.Element`, that element will be rendered, with size/color/title props cloned into it
- If given a React element type, it will be rendered with the other icon props
  As a consumer, you should never use `<IconWrapper icon={<element />}` directly; simply render `<element />` instead.}

\item{size}{Numeric. Size of the icon, in pixels.
Icons contains 16px and 20px SVG icon paths,
and chooses the appropriate resolution based on this prop.}

\item{title}{Character. Description string.
Browsers usually render this as a tooltip on hover, whereas screen
readers will use it for aural feedback.
By default, this is set to the icon's name for accessibility.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

