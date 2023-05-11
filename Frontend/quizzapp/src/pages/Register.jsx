import React, { useState } from "react";
import { useContext } from "react";
import { UserContext } from "../App";

import Subtitle from '../components/Subtitle';
import Button from '../components/Button';
import TextInput from '../components/TextInput';
import Range from '../components/Range';
import '../styles/Register.css';
import axios from "axios";

const Register = (props) => {

    const [user, setUser, , setQuestions] = useContext(UserContext);
    const [numQuestions, setNumQuestions] = useState();

    const handleChangeUsername = (event) => {
      setUser(event.target.value);
    };

    const handleNumQuestionsChange = (event) => {
      setNumQuestions(event.target.value);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const questions = await axios.get('http://127.0.0.1:5000/getAllQuestions', {});
        setQuestions(questions.data.Items);
        setUser(user);
        props.setPage(props.page+1)
    };

    return (
        <div className="container">
            <Subtitle text="QuizApp" />
            <form className="form" onSubmit={handleSubmit}>
                <div className="form-element">
                    <TextInput id="username" name="Input" label="Insert Username" placeholder="Here!" value={user} onChange={handleChangeUsername}/>
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
