import React from "react";
import "../styles/Button.css";

function Button(props) {
    return (
        <div className="button-container">
            <button className="Button" onClick={props.onClick}>
                {props.label}
            </button>
        </div>

    );
}

export default Button;
