import React, { Fragment} from 'react';
import '../styles/Feedback.css';

function Feedback(props) {
    const handleOnClick = () => {
        props.setModal(!props.modal); 
    }

  return (
    <div className='feedback'>
        <div className="modal" id="modal">
            <h2 className='modal-title'>{props.title ? props.title : "Modal Title"}</h2>
            <div className="content">
                <div className={props.status ? 'status green' : 'status red'}>{props.status ? "¡Correct!" : "¡Incorrect!"}</div>
                <p className='description'>
                    {props.content ? props.content : "Modal Content"}
                </p>
            </div>
            <div className="actions">
                <button className="toggle-button" onClick={handleOnClick}>Next Question</button>
            </div>
        </div>
    </div>
  )
}

export default Feedback