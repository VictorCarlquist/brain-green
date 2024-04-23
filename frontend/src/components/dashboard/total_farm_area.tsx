import { Badge, Card } from "react-bootstrap";
import { useTotalfarmareaQuery } from "../../redux/reducers/api";

function TotalFarmArea() {
  const {data = 0} = useTotalfarmareaQuery();

  return (
     <Card body>
      <h3>Área Total (ha)</h3>
      <h1><Badge bg="primary">{data}</Badge> </h1>
    </Card>
  );
}

export default TotalFarmArea;