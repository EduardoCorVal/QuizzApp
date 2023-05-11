import React from "react";
import "../styles/Row.css";

function Row(props){
    return (
        <tr className="row">{props.name} - {props.score}</tr>
    );
}

export default Row;