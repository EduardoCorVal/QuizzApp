import React from "react";
import "../styles/Range.css";

function Range(props) {
  return (
    <div className="Range">
      <label htmlFor={props.id}>{props.label}</label>
      <input
        type="range"
        id={props.id}
        name={props.name}
        value={props.value}
        min={props.min}
        max={props.max}
        step={props.step}
        onChange={props.onChange}
      />
      <output htmlFor={props.id} className="Range-value">
        {props.value}
      </output>
    </div>
  );
}

export default Range;
