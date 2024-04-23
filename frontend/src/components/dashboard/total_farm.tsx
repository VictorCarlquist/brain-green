import { Badge, Card } from "react-bootstrap";
import { useTotalfarmQuery } from "../../redux/reducers/api";

function TotalFarm() {
  const {data = 0} = useTotalfarmQuery();

  return (
    <Card body>
      <h3>Total de Fazendas</h3>
      <h1><Badge bg="primary">{data}</Badge> </h1>
    </Card>
  );
}

export default TotalFarm;