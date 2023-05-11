import React, {useContext} from 'react';
import '../styles/Header.css';
import { UserContext } from '../App';


const Header = (props) => {
  const [user, , , , score] = useContext(UserContext);
  return (
    <div className='header'>
        <h1>{user ? user : '---'}</h1>
        <h1>{props.title ? props.title : 'Quiz App'}</h1>
        <h1>{score ? score : '0'}</h1>
    </div>
  )
}

export default Header
