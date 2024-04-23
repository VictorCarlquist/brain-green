import { useState } from 'react';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Toast from 'react-bootstrap/Toast';

function ToastAutohide(props: {title: string, msg: string}) {
  const [show, setShow] = useState(false);

  return (
    <Row>
      <Col xs={6}>
        <Toast onClose={() => setShow(false)} show={show} delay={3000} autohide>
          <Toast.Header>
            <img
              src="holder.js/20x20?text=%20"
              className="rounded me-2"
              alt=""
            />
            <strong className="me-auto">{props.title}</strong>
            <small></small>
          </Toast.Header>
          <Toast.Body>{props.msg}</Toast.Body>
        </Toast>
      </Col>
    </Row>
  );
}

export default ToastAutohide;