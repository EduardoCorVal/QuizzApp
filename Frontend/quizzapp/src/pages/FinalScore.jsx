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


    const getBoard = async () => { 
        const result = await axios.get('http://127.0.0.1:5000/getTop10Users');
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