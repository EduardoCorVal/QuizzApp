/* Authors */
// Final Project: Quiz Application with Microservices
// Date: 28-Nov-2022
// Authors:
//          A01751587 Paulo Ogando Gulias 

import React, { Fragment, useContext } from "react";
import { UserContext } from "../App";

import "../styles/Question.css";
import Subtitle from "./Subtitle";
import Feedback from "./Feedback";
import imageExample from "../images/example.png";

const Question = (props) => {
  const [feedback, setFeedback] = React.useState(false);
  const [correct, setCorrect] = React.useState(false);
  const [user, , questions, , score, setScore] = useContext(UserContext);
  const [indexQ, setIndexQ] = React.useState(questions.length-1);
  const [feedbackText, setFeedbackText] = React.useState("");

  const checkAnswer = (option) => {
    if (questions[indexQ].Choices[option] === questions[indexQ].CorrectAnswer) {
      setCorrect(true);
      setScore(score + 10);
      setFeedbackText("Nice "+user+"! You got it right!");
    }
    else {
      setCorrect(false);
      setFeedbackText("Oops "+user+"! You got it wrong! The correct answer was: " + questions[indexQ].CorrectAnswer);

    }
    setFeedback(true);
  };

  return (
    <Fragment>
      {feedback ? <Feedback modal={feedback} title={questions[indexQ].Sentence} setModal={setFeedback} status={correct} content={feedbackText} indexQ={indexQ} setIndexQ={setIndexQ} page={props.page} setPage = {props.setPage}/> :
      <div className="question">
        <div className="question-text">
          <Subtitle text={questions[indexQ].Sentence} />
        </div>
        <div className="question-image">
          <img src={imageExample} alt="question"/>
        </div>
        <div className="options">
          {
            questions[indexQ].Choices.map((choice, index) => {
             return (
              <button key={index} onClick={()=>{checkAnswer(index)}}>
                {choice}
              </button>
             );
          })}
        </div>
      </div>
    }
    </Fragment>
  );
};

export default Question;
