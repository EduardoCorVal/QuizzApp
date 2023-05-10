import Button from "../components/Button";
import Header from "../components/Header";
import LeaderBoard from "../components/LeaderBoard"
import Subtitle from "../components/Subtitle";
const FinalScore = (props) => {
    return (
        <div>
        <Header 
        user = " "
        score = " "/>
        <Subtitle text={props.user + " - " + props.score} />
        <LeaderBoard
            user1 = {props.user1 + " - " + props.score1}
            user2 = {props.user2 + " - " + props.score2}
            user3 = {props.user3 + " - " + props.score3}
            user4 = {props.user4 + " - " + props.score4}
            user5 = {props.user5 + " - " + props.score5}
            user6 = {props.user6 + " - " + props.score6}
            user7 = {props.user7 + " - " + props.score7}
            user8 = {props.user8 + " - " + props.score8}
            user9 = {props.user9 + " - " + props.score9}
            user10 = {props.user10 + " - " + props.score10}/>
        <Button label ="Restart App"/>
        
      </div>
    )
}

export default FinalScore;