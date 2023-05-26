/* Authors */
// Final Project: Quiz Application with Microservices
// Date: 28-Nov-2022
// Authors:
//          A01745419 José Luis Madrigal Sánchez

import React from "react";
import "../styles/LeaderBoard.css";
import Row from "./Row";

function LeaderBoard(props) {
    return (
        <div className="button-container">
            <table id="leaderboard">
                <tr className="column">LeaderBoard</tr>
                {props.arrUsuarios.map(user=>{
                    return (<Row
                    name = {user.name}
                    score = {user.score}/>)
                })}
            </table>
        </div>

    );
}

export default LeaderBoard;