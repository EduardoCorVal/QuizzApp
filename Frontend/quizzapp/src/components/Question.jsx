import React from "react";
import "../styles/Question.css";
import Subtitle from "./Subtitle";

const Question = (props) => {
  return (
    <div className="question">
      <div className="question-text">
        <Subtitle text={props.question} />
      </div>
      <div className="question-image">
        <img src={props.image} alt="question"/>
      </div>
      <div className="options">
        <button onClick={() => props.checkAnswer(props.option1)}>
            {props.option1}
        </button>
        <button onClick={() => props.checkAnswer(props.option2)}>
          {props.option2}
        </button>
        <button onClick={() => props.checkAnswer(props.option3)}>
          {props.option3}
        </button>
        <button onClick={() => props.checkAnswer(props.option4)}>
          {props.option4}
        </button>
      </div>
    </div>
  );
};

export default Question;
