import React, {Component} from 'react';
import PropTypes from 'prop-types';
import { Button } from 'evergreen-ui';
import { omit } from "ramda";
import { renderDashComponents } from "dash-extensions-js";
import { InfoSignIcon, EditIcon } from 'evergreen-ui';


const defaultProps = {
    label: '',
    size: 'medium',
    onClick: () => {},
    intent:"none",
    appearance:"default",
    isActive: true,
    iconBefore: false,
    isLoading: false,
    n_clicks:0,
    // n_clicks_previous:0,
    setProps: () => {},
};


export default class button extends Component {
    constructor(props, Props) {
        super(props);
        this.state = {disabled: props.disabled,
                      n_clicks: props.n_clicks,
                      // n_clicks_previous: props.n_clicks_previous
                  };
      }

    handleClick() {
        const n = this.props.n_clicks + 1
        if (this.props.setProps) this.props.setProps({n_clicks: n});
        // if (this.props.setProps) this.props.setProps({n_clicks_previous: n});
        if (this.setState) this.setState({n_clicks: n});
        // if (this.setState) this.setState({n_clicks_previous: n});
      }

    render() {
        const {id, label, setProps, value, intent, appearance, size, isActive, isLoading, iconBefore, iconAfter, n_clicks,children} = this.props;
        let onClick
        // this is the function that sets n_clicks
        if (this.props.setProps){
          onClick = this.handleClick.bind(this)
        } else {
          onClick = null
        }
        return (
            <div id={id}>
                <Button
                    label={label}
                    size={size}
                    onClick={onClick}
                    intent={intent}
                    appearance={appearance}
                    isActive={isActive}
                    iconBefore={iconBefore}
                    isLoading={isLoading}
                    n_clicks={n_clicks}
                    // n_clicks_previous={n_clicks_previous}
                    >
                    {this.props.children}
                </Button>
            </div>
        );
    };
};

button.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * A label that will be printed when this component is rendered.
     */
    label: PropTypes.string.isRequired,

    /**
     * The value displayed in the input.
     */
    value: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    size: PropTypes.oneOf(["small", "medium", "large"]),
    /**
     * The size of the button
     */
    intent: PropTypes.string,
    /**
     * One of "none", "success", or "danger". The default is none.
     */
    appearance: PropTypes.string,
    /**
     * The evergreen appearance property, "default", "primary", or "minimal"
     */
    isLoading: PropTypes.bool,
    /**
     * if true, this will show a loading indicator and disable the button
     */
    isActive: PropTypes.bool,
    /**
     * A label that will be printed when this component is rendered.
     */
    iconBefore: PropTypes.element,
    /**
     * Sets an icon before the text. Can be any icon from Evergreen or a custom element.
     */ 
    iconAfter: PropTypes.element,
    /**
     * Sets an icon after the text. Can be any icon from Evergreen or a custom element.
     */ 
    disabled: PropTypes.bool,
    /**
     * When true, the button is disabled. isLoading also sets the button to disabled
     */ 
    className: PropTypes.string,
    /**
     * Class name passed to the button
     */ 
    n_clicks: PropTypes.number,
    /**
     * The number of clicks the button has recieved this sesson.
     */
    children: PropTypes.string,
        /**
     * The actual text on the button
     */
    setProps: PropTypes.func
};
button.defaultProps = defaultProps;
