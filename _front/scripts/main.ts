import 'bootstrap';
import '../styles/main.scss';

export const greet = () => {
  return "Hello World...";
}

const main = () => {
  console.log(greet());
};

main();
