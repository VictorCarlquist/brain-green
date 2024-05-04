import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { login } from "./login";

export interface LoginData {
  username: string;
  password: string;
}

export interface LoginResponse {
  refresh: string;
  access: string;
}

export interface ProducerData {
    id: number,
    cpf_cnpj: string,
    name: string
}

export interface FarmData {
  id: number,
  producer_id: number,
  farm_name: string,
  city: string,
  state: string,
  total_area_hectares: number
}

export interface AreaData {
  id: number,
  farm_id: number,
  area_type: string,
  area_hectares: number,
  crops: string
}

export interface PieByState {
  state: string,
  total: number
}

export interface PieByCrop {
  areafarm__crops: string,
  total: number
}

export interface PieByAreaType{
  areafarm__area_type: string,
  total: number
}

export const apiSlice = createApi({
    reducerPath: "loginApi",
    baseQuery: fetchBaseQuery({
        baseUrl: "http://35.192.131.238:8000",
        prepareHeaders(headers) {
            let access = localStorage.getItem("access");
            if (!access)
                access = ""
            headers.set("Authorization", "Bearer " + access );
        }
    }),
    tagTypes: ['farmList', 'areaList', 'producerlist'],
    endpoints: (builder) => ({
        login: builder.mutation<LoginResponse, Partial<LoginData>>({
          query: (credentials) => ({
            url: "/token/",
            method: "POST",
            body: credentials,
          }),
          transformResponse: (response: LoginResponse) => {
            localStorage.setItem("access", response.access);
            localStorage.setItem("refresh", response.refresh);
            return response;
          },
          onQueryStarted: async (_, api) => {
            const { dispatch, queryFulfilled } = api;
            await queryFulfilled;
            dispatch(login());
          },
        }
      ),

      totalfarm: builder.query<number | void, number | void>({
        query(){
          return '/dashboard/total-farm'
        }
      }),
      totalfarmarea: builder.query<number | void, number | void>({
        query(){
          return '/dashboard/total-area'
        }
      }),
      totalByState: builder.query<PieByState[], void>({
        query() {
          return '/dashboard/total-state';
        },
      }),
      totalByCrops: builder.query<PieByCrop[], void>({
        query() {
          return '/dashboard/total-crop';
        },
      }),
      totalByTypeArea: builder.query<PieByAreaType[], void>({
        query() {
          return '/dashboard/total-type';
        },
      }),
      updateFarm: builder.mutation<void, Partial<FarmData>>({
          query: (farm) => ({
            url: "/farm/" + farm.id,
            method: "PUT",
            body: farm,
          }),
        }
      ),
      farmList: builder.query<FarmData[], number>({
        query(producer_id: number) {
            return '/farm-list/' + producer_id
        },
        providesTags: ['farmList'],
      }),
      deleteFarm: builder.mutation<FarmData, number>({
        query: (id) => ({
          url: "/farm/" + id,
          method: "DELETE",
        }),
        invalidatesTags: ['farmList'],
      }),
      addFarm: builder.mutation<void, Partial<FarmData>>({
        query: (farm) => ({
          url: "/farm/",
          method: "POST",
          body: farm,
        }),
        invalidatesTags: ['farmList'],
      }),
      areaList: builder.query<AreaData[], number>({
        query(farm_id: number) {
            return '/area-list/' + farm_id
        },
        providesTags: ['areaList'],
      }),
      deleteArea: builder.mutation<void, number>({
        query: (area_id) => ({
          url: "/area/" + area_id,
          method: "DELETE",
        }),
        invalidatesTags: ['areaList'],
      }),
      addArea: builder.mutation<void, Partial<AreaData>>({
        query: (farm) => ({
          url: "/area/",
          method: "POST",
          body: farm,
        }),
        invalidatesTags: ['areaList'],
      }),
      updateArea: builder.mutation<void, Partial<AreaData>>({
        query: (area) => ({
          url: "/area/" + area.id,
          method: "PUT",
          body: area,
        }),
      }),
      producerlist: builder.query<ProducerData[], number | void>({
        query() {
            return '/producer/'
        },
        providesTags: ['producerlist'],
      }),
      deleteProducer: builder.mutation<void, number>({
        query: (id) => ({
          url: "/producer/" + id,
          method: "DELETE",
        }),
        invalidatesTags: ['producerlist'],
      }),
      addProducer: builder.mutation<void, Partial<ProducerData>>({
        query: (producer) => ({
          url: "/producer/",
          method: "POST",
          body: producer,
        }),
        invalidatesTags: ['producerlist'],
      }),
      updateProducer: builder.mutation<void, Partial<ProducerData>>({
        query: (producer) => ({
          url: "/producer/" + producer.id,
          method: "PUT",
          body: producer,
        }),
      }),
    }),
  })
  
  export const {
    useLoginMutation,

    useTotalfarmQuery,
    useTotalfarmareaQuery,
    useTotalByStateQuery,
    useTotalByCropsQuery,
    useTotalByTypeAreaQuery,

    useFarmListQuery,
    useUpdateFarmMutation,
    useDeleteFarmMutation,
    useAddFarmMutation,

    useAddAreaMutation,
    useAreaListQuery,
    useDeleteAreaMutation,
    useUpdateAreaMutation,

    useProducerlistQuery,
    useDeleteProducerMutation,
    useAddProducerMutation,
    useUpdateProducerMutation,

  } = apiSlice;
