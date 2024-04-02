
import Form from "../components/Form"
import ParticlesBack from "../components/ParticlesBack"
function Login(){    
    return <>
    <ParticlesBack/>
    <Form route="/api/token/" method="login"/>
    </>
}

export default Login

