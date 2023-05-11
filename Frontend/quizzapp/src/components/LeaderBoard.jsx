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