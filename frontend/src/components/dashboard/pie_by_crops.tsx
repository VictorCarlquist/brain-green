import { Card } from "react-bootstrap";
import { useTotalByCropsQuery } from "../../redux/reducers/api";
import { PieChart } from '@mui/x-charts/PieChart';


function PieByCrops() {
  const {data = []} = useTotalByCropsQuery();
  const pieData = data.map(item => ({label: item.areafarm__crops, value: item.total}));

  return (
    <Card body>
      <h2>Área por Cultura (ha)</h2>
      <center>
        <PieChart
          series={[
            {
              data: pieData,
            },
            ]}
            width={300}
            height={200}
        />
     </center>
    </Card>

  );
}

export default PieByCrops;