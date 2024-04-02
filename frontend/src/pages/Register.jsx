import Form from '../components/Form';
import ParticlesBack from "../components/ParticlesBack"

function Register(){    
    return <>
    <ParticlesBack/>
    <Form route="/api/user/register/" method="register"/>
    </> 
}
export default Register