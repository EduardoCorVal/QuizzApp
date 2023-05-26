/* Authors */
// Final Project: Quiz Application with Microservices
// Date: 28-Nov-2022
// Authors:
//          A01751587 Paulo Ogando Gulias 

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
