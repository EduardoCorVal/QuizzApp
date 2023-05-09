import React, { useState } from "react";

import Subtitle from '../components/Subtitle';
import Button from '../components/Button';
import TextInput from '../components/TextInput';
import Range from '../components/Range';
import '../styles/Register.css';

const Register = () => {

    const [username, setUsername] = useState("");
    const [numQuestions, setNumQuestions] = useState(6);

    const handleChangeUsername = (event) => {
      setUsername(event.target.value);
    };

    const handleNumQuestionsChange = (event) => {
      setNumQuestions(event.target.value);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        alert(`Username ${username}. Questions ${numQuestions}`);
    };

    return (
        <div className="container">
            <Subtitle text="QuizApp" />
            <form className="form" onSubmit={handleSubmit}>
                <div className="form-element">
                    <TextInput id="username" name="Input" label="Insert Username" placeholder="Here!" value={username} onChange={handleChangeUsername}/>
                </div>
                <div className="form-element">
                    <Range id="number-questions" name="range" label="How many questions" value={numQuestions} min={1} max={10} step={1} onChange={handleNumQuestionsChange}/>
                </div>
                <div className="form-element">
                    <Button label="Start" type="submit" />
                </div>
            </form>
        </div>
    )
}

export default Register;
