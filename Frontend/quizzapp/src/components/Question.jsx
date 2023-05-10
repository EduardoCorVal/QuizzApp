import React, { Fragment } from "react";
import "../styles/Question.css";
import Subtitle from "./Subtitle";
import Feedback from "./Feedback";

const Question = (props) => {
  const [feedback, setFeedback] = React.useState(false);
  const [correct, setCorrect] = React.useState(false);

  const checkAnswer = (option) => {
    if (option === props.answer) {
      setCorrect(true);
    }
    else {
      setCorrect(false);
    }
    setFeedback(true);
  };


  return (
    <Fragment>
      {feedback ? <Feedback modal={feedback} title={props.question} setModal={setFeedback} status={correct}/> :
      <div className="question">
        <div className="question-text">
          <Subtitle text={props.question} />
        </div>
        <div className="question-image">
          <img src={props.image} alt="question"/>
        </div>
        <div className="options">
          <button onClick={()=>{checkAnswer(props.option1)}}>
              {props.option1}
          </button>
          <button onClick={()=>{checkAnswer(props.option2)}}>
            {props.option2}
          </button>
          <button onClick={()=>{checkAnswer(props.option3)}}>
            {props.option3}
          </button>
          <button onClick={()=>{checkAnswer(props.option4)}}>
            {props.option4}
          </button>
        </div>
      </div>
    }
    </Fragment>
  );
};

export default Question;
