/* Authors */
// Final Project: Quiz Application with Microservices
// Date: 28-Nov-2022
// Authors:
//          A01745865 José Ángel García Gómez 

import React, {useContext} from 'react';
import { UserContext } from '../App';
import axios from 'axios';

import '../styles/Feedback.css';
const backendURL = process.env.REACT_APP_BACKEND_URL;

function Feedback(props) {
    const [user, , , , score,] = useContext(UserContext);
    const handleOnClick = () => {
        if (props.indexQ - 1 < 0) {
            const postUser = async () => {
                await axios.post(`${backendURL}/user`, {
                    name: user,
                    points: score
                })}
            postUser();
            props.setPage(props.page + 1);
        }
        else {
            props.setIndexQ(props.indexQ - 1);
            props.setModal(!props.modal); 
        }
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