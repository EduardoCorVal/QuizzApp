import React, {useContext, useState} from "react";
import { UserContext } from "../App";
import axios from "axios";

import Button from "../components/Button";
import Header from "../components/Header";
import LeaderBoard from "../components/LeaderBoard"
import Subtitle from "../components/Subtitle";


const FinalScore = (props) => {
    const [user, setUser, , , score, setScore] = useContext(UserContext);
    const [users, setUsers] = useState(null);
    const [post, setPost] = useState(false);

    const postUser = async () => {
        const result = await axios.post('http://127.0.0.1:5000/user', {
            name: user,
            points: score
        });
    };

    const getBoard = async () => { 
        const result = await axios.get('http://127.0.0.1:5000/getAllUsers');
        const newUsers = [];
        result.data.Items.forEach((user) => {
            newUsers.push({name: user.name, score: user.points});
        });
        setUsers(newUsers);
    }
    if (!post){
        postUser();
        getBoard();
        setPost(true);
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