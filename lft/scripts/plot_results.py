import json, matplotlib.pyplot as plt
d=json.load(open("results/metrics.json"))
r=d["rouge"]["rougeL"].mid.fmeasure if "rougeL" in d["rouge"] else 0
wins=sum(1 for x in d["results"] if isinstance(x,dict) and x.get("winner")=="student")
plt.bar(["ROUGE-L"],[r])
plt.title(f"ROUGE-L={r:.3f}, Student WinRate={wins/len(d['results']):.2f}")
plt.savefig("results/summary_plot.png")
print("✅ Saved plot to results/summary_plot.png")
