import React from "react";
import "../styles/LeaderBoard.css";

function LeaderBoard(props) {
    return (
        <div className="button-container">
            <table>
                <tr className="column">LeaderBoard</tr>
                <tr className="odd">{props.user1}</tr>
                <tr className="even">{props.user2}</tr>
                <tr className="odd">{props.user3}</tr>
                <tr className="even">{props.user4}</tr>
                <tr className="odd">{props.user5}</tr>
                <tr className="even">{props.user6}</tr>
                <tr className="odd">{props.user7}</tr>
                <tr className="even">{props.user8}</tr>
                <tr className="odd">{props.user9}</tr>
                <tr className="even">{props.user10}</tr>
            </table>
        </div>

    );
}

export default LeaderBoard;