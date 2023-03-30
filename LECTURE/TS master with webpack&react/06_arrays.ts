// String array
const activeUsers: string[] = [];
activeUsers.push("Tony");

// Number array
const ageList: number[] = [45, 56, 13];
ageList[0] = 99;

// 다른 배열 구문
// const bools: Array<boolean> = []
const bools: boolean[] = [];

type Point = {
  x: number;
  y: number;
};

const coords: Point[] = [];
coords.push({ x: 23, y: 8 });

// 다차원 배열
const board: string[][] = [
  ["X", "O", "X"],
  ["X", "O", "X"],
  ["X", "O", "X"],
];

const demo: number[][][] = [[[1]]]
