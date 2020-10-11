﻿#pragma once

#include "NeuronBase.h"
#include "SynapseBase.h"
#include <vector>
#include <atomic>
#ifndef CompilingNeuronWrapper
#include <concurrent_queue.h>
#endif
#include <string>
#define NeuronWrapper _

namespace NeuronEngine
{
	class NeuronArrayBase
	{
	public:
		__declspec(dllexport) NeuronArrayBase();
		__declspec(dllexport) ~NeuronArrayBase();
		__declspec(dllexport) void Initialize(int theSize, NeuronBase::modelType t = NeuronBase::modelType::Std);
		__declspec(dllexport) NeuronBase* GetNeuron(int i);
		__declspec(dllexport) int GetArraySize();
		__declspec(dllexport) long long GetTotalSynapseCount();
		__declspec(dllexport) long GetNeuronsInUseCount();
		__declspec(dllexport) void Fire();
		__declspec(dllexport) long long GetGeneration();
		__declspec(dllexport) int GetFiredCount();
		__declspec(dllexport) int GetThreadCount();
		__declspec(dllexport) void SetThreadCount(int i);
		__declspec(dllexport) void GetBounds(int taskID, int& start, int& end);
		__declspec(dllexport) std::string GetRemoteFiringString();
		__declspec(dllexport) SynapseBase GetRemoteFiringSynapse();


	private:
		int arraySize = 0;
		int threadCount = 124;//TODO
		std::vector<NeuronBase> neuronArray;
		std::atomic<long> firedCount = 0;
		long generation = 0;

		static std::vector<unsigned long long> fireList1;
		static std::vector<unsigned long long> fireList2;
		static int fireListCount;

	private:
		__declspec(noinline) void ProcessNeurons1(int taskID); //these are noinlined so the profiler makes more sense
		__declspec(noinline) void ProcessNeurons2(int taskID);
	public:
		static void AddNeuronToFireList1(int id);
		static bool clearFireListNeeded;
		static void ClearFireLists();

	public:
#ifndef CompilingNeuronWrapper
		static concurrency::concurrent_queue<SynapseBase> remoteQueue;
		static concurrency::concurrent_queue<NeuronBase *> fire2Queue;
#endif // !NeuronWrapper
	};
}