import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

import { useEffect, useState } from 'react';
import { useLoginMutation } from '../redux/reducers/api';

function Login() {

    const [login, { isLoading }] = useLoginMutation();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    useEffect(() => {
        if (localStorage.getItem('access') === null) {
            window.location.href = '/'
        }
    }, []);

    return (
        <>
        <Form>
        <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Label>Email address</Form.Label>
            <Form.Control type="email" placeholder="Enter email" value={email} onChange={(e) => setEmail(e.target.value)}/>
            <Form.Text className="text-muted" >
            We'll never share your email with anyone else.
            </Form.Text>
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
            <Form.Label>Password</Form.Label>
            <Form.Control type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)}/>
        </Form.Group>
        <Button
            onClick={async () => {
                try {
                    await login({username: email, password: password}).unwrap();
                    window.location.href = '/dashboard';
                } catch (error) {
                    console.error(error);
                }
            }}
            disabled={isLoading}
        variant="primary" type="submit">
            Submit
        </Button>
        </Form>
        </>
    );
}

export default Login;