// parseCallGraph.ts
import * as fs from "fs";

interface Component {
  name: string;
  functions: string[];
  events: string[];
}

interface CallOrder {
  pred: string;
  succ: string;
}

interface CallGraph {
  components: Component[];
  order: CallOrder[];
}

function loadCallGraph(path: string): CallGraph {
  const rawData = fs.readFileSync(path, "utf-8");
  const parsed = JSON.parse(rawData);

  const graph: CallGraph = {
    components: (parsed.components || []).map((c: any) => ({
      name: c.name,
      functions: c.functions || [],
      events: c.events || [],
    })),
    order: (parsed.order || []).map((o: any) => ({
      pred: o.pred,
      succ: o.succ,
    })),
  };

  return graph;
}

function printCallGraph(graph: CallGraph) {
  console.log("📦 组件列表:");
  for (const c of graph.components) {
    console.log(`- ${c.name}`);
    console.log(`  functions: ${c.functions.join(", ")}`);
    console.log(`  events: ${c.events.join(", ")}`);
  }

  console.log("\n🔗 调用顺序:");
  for (const o of graph.order) {
    console.log(`  ${o.pred} -> ${o.succ}`);
  }
}

// 主函数
function main() {
  const filePath = process.argv[2] || "./example_callgraph.json";
  const graph = loadCallGraph(filePath);
  printCallGraph(graph);
}

main();
