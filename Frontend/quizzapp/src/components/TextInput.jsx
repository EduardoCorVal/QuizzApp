import React from "react";
import "../styles/TextInput.css";

function TextInput(props) {
  return (
    <div className="TextInput">
      <label htmlFor={props.id}>{props.label}</label>
      <input
        type="text"
        id={props.id}
        name={props.name}
        value={props.value}
        onChange={props.onChange}
        placeholder={props.placeholder}
      />
    </div>
  );
}

export default TextInput;
