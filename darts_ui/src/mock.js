export const getDart = () => {
  const double = Math.random() < 0.1;
  const triple = Math.random() < 0.05;
  const section = Math.floor(Math.random() * 20) + 1;
  return {
    section,
    double,
    triple,
  };
};
