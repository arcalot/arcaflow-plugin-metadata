# Python Plugin Metadata

This is a simple plugin that collects all data from ansible-facts and outputs it.

Install via Poetry:
```
python3 -m poetry install --without dev
```
Run by executing the following command:
```
python3 metadata_plugin.py
```

# Autogenerated Input/Output Documentation by Arcaflow-Docsgen Below

<!-- Autogenerated documentation by arcaflow-docsgen -->
## Collect Metadata (`collect-metadata`)

Collects ansible facts metadata

### Input

<table><tbody>
<tr><th>Type:</th><td><code>scope</code></td><tr><th>Root object:</th><td>InputParams</td></tr>
<tr><th>Properties</th><td></td></tr>
<tr><td colspan="2"><details><summary><strong>Objects</strong></summary><details><summary>InputParams (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td></td></tr>
</tbody></table>
        </details></details></td></tr>
</tbody></table>

### Outputs


#### error

<table><tbody>
<tr><th>Type:</th><td><code>scope</code></td><tr><th>Root object:</th><td>ErrorOutput</td></tr>
<tr><th>Properties</th><td><details><summary>error (<code>string</code>)</summary>
                <table><tbody><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details></td></tr>
<tr><td colspan="2"><details><summary><strong>Objects</strong></summary><details><summary>ErrorOutput (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td><details><summary>error (<code>string</code>)</summary>
        <table><tbody><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details></td></tr>
</tbody></table>
        </details></details></td></tr>
</tbody></table>

#### success

<table><tbody>
<tr><th>Type:</th><td><code>scope</code></td><tr><th>Root object:</th><td>SelectedFacts</td></tr>
<tr><th>Properties</th><td><details><summary>architecture (<code>string</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>ansible architecture</td></tr><tr><th>Description:</th><td width="500">The system architecture</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details><details><summary>env (<code>map[<code>string</code>,<code>string</code>]</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>ansible env</td></tr><tr><th>Description:</th><td width="500">The system environment variables</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>map[<code>string</code>,<code>string</code>]</code></td><tr><td colspan="2">
    <details>
        <summary>Key type</summary>
        <table><tbody><tr><th>Type:</th><td><code>string</code></td></tbody></table>
    </details>
</td></tr>
<tr><td colspan="2">
    <details>
        <summary>Value type</summary>
        <table><tbody><tr><th>Type:</th><td><code>string</code></td></tbody></table>
    </details>
</td></tr>
</tbody></table>
            </details><details><summary>fqdn (<code>string</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>ansible fqdn</td></tr><tr><th>Description:</th><td width="500">The system fully-qualified domain name</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details><details><summary>kernel (<code>string</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>ansible kernel</td></tr><tr><th>Description:</th><td width="500">The system OS kernel</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details><details><summary>memtotal_mb (<code>int</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>ansible memtotal MB</td></tr><tr><th>Description:</th><td width="500">The system total memory in MB</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>int</code></td>
</tbody></table>
            </details><details><summary>processor (<code>list[<code>string</code>]</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>ansible processor</td></tr><tr><th>Description:</th><td width="500">The system processor list</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>list[<code>string</code>]</code></td><tr><td colspan="2">
    <details>
        <summary>List items</summary>
        <table><tbody><tr><th>Type:</th><td><code>string</code></td></tbody></table>
    </details>
</td></tr></tbody></table>
            </details><details><summary>processor_cores (<code>int</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>ansible processor cores</td></tr><tr><th>Description:</th><td width="500">The system total processor cores</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>int</code></td>
</tbody></table>
            </details><details><summary>processor_count (<code>int</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>ansible processor count</td></tr><tr><th>Description:</th><td width="500">The system total processor count</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>int</code></td>
</tbody></table>
            </details><details><summary>processor_threads_per_core (<code>int</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>ansible processor threads per core</td></tr><tr><th>Description:</th><td width="500">The system threads per processor core</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>int</code></td>
</tbody></table>
            </details><details><summary>product_name (<code>string</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>ansible product name</td></tr><tr><th>Description:</th><td width="500">The system product name</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details><details><summary>product_version (<code>string</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>ansible product version</td></tr><tr><th>Description:</th><td width="500">The system product version</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details><details><summary>swaptotal_mb (<code>int</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>ansible swaptotal mb</td></tr><tr><th>Description:</th><td width="500">The system swap size in MB</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>int</code></td>
</tbody></table>
            </details><details><summary>system_vendor (<code>string</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>ansible system vendor</td></tr><tr><th>Description:</th><td width="500">The system vendor</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details><details><summary>uptime_seconds (<code>int</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>ansible uptime seconds</td></tr><tr><th>Description:</th><td width="500">The system uptime in seconds</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>int</code></td>
</tbody></table>
            </details></td></tr>
<tr><td colspan="2"><details><summary><strong>Objects</strong></summary><details><summary>SelectedFacts (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td><details><summary>architecture (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>ansible architecture</td></tr><tr><th>Description:</th><td width="500">The system architecture</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details><details><summary>env (<code>map[<code>string</code>,<code>string</code>]</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>ansible env</td></tr><tr><th>Description:</th><td width="500">The system environment variables</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>map[<code>string</code>,<code>string</code>]</code></td><tr><td colspan="2">
    <details>
        <summary>Key type</summary>
        <table><tbody><tr><th>Type:</th><td><code>string</code></td></tbody></table>
    </details>
</td></tr>
<tr><td colspan="2">
    <details>
        <summary>Value type</summary>
        <table><tbody><tr><th>Type:</th><td><code>string</code></td></tbody></table>
    </details>
</td></tr>
</tbody></table>
        </details><details><summary>fqdn (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>ansible fqdn</td></tr><tr><th>Description:</th><td width="500">The system fully-qualified domain name</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details><details><summary>kernel (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>ansible kernel</td></tr><tr><th>Description:</th><td width="500">The system OS kernel</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details><details><summary>memtotal_mb (<code>int</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>ansible memtotal MB</td></tr><tr><th>Description:</th><td width="500">The system total memory in MB</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>int</code></td>
</tbody></table>
        </details><details><summary>processor (<code>list[<code>string</code>]</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>ansible processor</td></tr><tr><th>Description:</th><td width="500">The system processor list</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>list[<code>string</code>]</code></td><tr><td colspan="2">
    <details>
        <summary>List items</summary>
        <table><tbody><tr><th>Type:</th><td><code>string</code></td></tbody></table>
    </details>
</td></tr></tbody></table>
        </details><details><summary>processor_cores (<code>int</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>ansible processor cores</td></tr><tr><th>Description:</th><td width="500">The system total processor cores</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>int</code></td>
</tbody></table>
        </details><details><summary>processor_count (<code>int</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>ansible processor count</td></tr><tr><th>Description:</th><td width="500">The system total processor count</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>int</code></td>
</tbody></table>
        </details><details><summary>processor_threads_per_core (<code>int</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>ansible processor threads per core</td></tr><tr><th>Description:</th><td width="500">The system threads per processor core</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>int</code></td>
</tbody></table>
        </details><details><summary>product_name (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>ansible product name</td></tr><tr><th>Description:</th><td width="500">The system product name</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details><details><summary>product_version (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>ansible product version</td></tr><tr><th>Description:</th><td width="500">The system product version</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details><details><summary>swaptotal_mb (<code>int</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>ansible swaptotal mb</td></tr><tr><th>Description:</th><td width="500">The system swap size in MB</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>int</code></td>
</tbody></table>
        </details><details><summary>system_vendor (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>ansible system vendor</td></tr><tr><th>Description:</th><td width="500">The system vendor</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details><details><summary>uptime_seconds (<code>int</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>ansible uptime seconds</td></tr><tr><th>Description:</th><td width="500">The system uptime in seconds</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>int</code></td>
</tbody></table>
        </details></td></tr>
</tbody></table>
        </details></details></td></tr>
</tbody></table>
<!-- End of autogenerated documentation -->
