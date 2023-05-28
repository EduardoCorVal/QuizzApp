/* Authors */
// Final Project: Quiz Application with Microservices
// Date: 28-Nov-2022
// Authors:
//          A01746664 Eduardo Joel Cortez Valente
//          A01751587 Paulo Ogando Gulias 
//          A01745865 José Ángel García Gómez 
//          A01745419 José Luis Madrigal Sánchez

import React, {useContext, useState} from "react";
import { UserContext } from "../App";
import axios from "axios";

import Button from "../components/Button";
import Header from "../components/Header";
import LeaderBoard from "../components/LeaderBoard"
import Subtitle from "../components/Subtitle";

const backendURL = process.env.REACT_APP_BACKEND_URL;

const FinalScore = (props) => {
    const [user, setUser, , , score, setScore] = useContext(UserContext);
    const [users, setUsers] = useState(null);


    const getBoard = async () => { 
        const result = await axios.get(`${backendURL}/getTop10Users`);
        const newUsers = [];
        result.data.Items.forEach((user) => {
            newUsers.push({name: user.name, score: user.points});
        });
        setUsers(newUsers);
    }
    if (!users){
        setTimeout(getBoard, 1000);
    }


    return (
        <div>
            <Header 
            user = " "
            score = " "/>
            <Subtitle text={user + " : " + score} />   
            {users != null ? <LeaderBoard arrUsuarios={users}/> : <div> Loading... </div>}
            <Button label ="Restart App" onClick={()=>{
                props.setPage(0);
                setUser("");
                setScore(0);
            }}/>
      </div>
    )
}

export default FinalScore;