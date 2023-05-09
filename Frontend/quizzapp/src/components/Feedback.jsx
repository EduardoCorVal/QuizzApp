import React, { Fragment} from 'react';
import '../styles/Feedback.css';

function Feedback(props) {
    // const [modal, setModal] = useState(false) -> Esto se tiene que definir en el padre o en un contexto
    
    const modalStyle = "modal"; // props.modal ? "modal" : "modal off";
    const handleOnClick = () => {
        props.setModal(!props.modal); 
    }

  return (
    <Fragment>
        {/*<button class="toggle-button" id="centered-toggle-button" onClick={handleOnClick}>Toggle</button>} Definir el boton para mostrar en el padre*/} 
        <div class={modalStyle} id="modal">
            <h2>{props.title ? props.title : "Modal Title"}</h2>
            <div class="content">
                <div className={props.status ? 'status green' : 'status red'}>{props.status ? props.status : "¡Incorrect!"}</div>
                <p className='description'>
                    {props.content ? props.content : "Modal Content"}
                </p>
            </div>
            <div class="actions">
                <button class="toggle-button" onClick={handleOnClick}>Next Question</button>
            </div>
        </div>
    </Fragment>
  )
}

export default Feedback