/* Authors */
// Final Project: Quiz Application with Microservices
// Date: 28-Nov-2022
// Authors:
//          A01751587 Paulo Ogando Gulias 

import React from "react";
import "../styles/Row.css";

function Row(props){
    return (
        <tr className="row">{props.name} - {props.score}</tr>
    );
}

export default Row;