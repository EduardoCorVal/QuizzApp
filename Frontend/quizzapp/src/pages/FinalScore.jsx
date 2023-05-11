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
        <Subtitle text={props.actualUser.name + " - " + props.actualUser.score} />
        <LeaderBoard
            arrUsuarios = {props.boardUsers}/>
        <Button label ="Restart App"/>
      </div>
    )
}

export default FinalScore;