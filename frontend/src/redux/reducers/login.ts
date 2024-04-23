import { createSlice } from "@reduxjs/toolkit";


export interface UserState {
  loggedIn: boolean;
  router: string | undefined;
}

export const initialState: UserState = {
  loggedIn: false,
  router: "/",
};


export const loginReducer = createSlice({
  name: "login",
  initialState,
  reducers: {
    login: (state) => {
      state.loggedIn = true;
      state.router = "/dashboard";
    },
    logout: (state) => {
      state.loggedIn = false;
      state.router = "/";
    },
  },
});


export const { login, logout } = loginReducer.actions;
export default loginReducer.reducer;
