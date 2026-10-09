> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrations Catalog

> Browse over 2,000+ third-party integrations and APIs available via the Zenflow Pipedream catalog.

<Note>
  Integration requires a Zencoder account.
</Note>

An interactive directory of the over 2,000+ integrations available via the Pipedream MCP catalog and built-in connectors. Search or filter by category to discover how to connect your tools to Zenflow.

<style>
  {`
    :root {
      --cat-dropdown-bg: #ffffff;
      --cat-dropdown-border: #e2e8f0;
      --cat-dropdown-text: #1e293b;
      --cat-dropdown-hover: #f1f5f9;
    }
    .dark {
      --cat-dropdown-bg: #0b0f19;
      --cat-dropdown-border: #1e293b;
      --cat-dropdown-text: #f8fafc;
      --cat-dropdown-hover: #1e293b;
    }
    #category-options-list label {
      color: var(--cat-dropdown-text) !important;
      transition: background-color 0.2s;
    }
    #category-options-list label:hover {
      background-color: var(--cat-dropdown-hover) !important;
    }
    `}
</style>

<div style={{ marginTop: '24px' }}>
  <div style={{ marginBottom: '20px' }}>
    <input
      type="text"
      id="catalog-search"
      placeholder="Search 2,000+ integrations (e.g. Stripe, Salesforce, Airtable)..."
      style={{
    width: '100%',
    padding: '12px 16px',
    borderRadius: '8px',
    border: '1px solid var(--cat-dropdown-border)',
    backgroundColor: 'var(--cat-dropdown-bg)',
    color: 'var(--cat-dropdown-text)',
    fontSize: '16px',
    outline: 'none',
    boxShadow: '0 1px 2px 0 rgba(0, 0, 0, 0.05)'
  }}
    />
  </div>

  <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', marginBottom: '24px' }}>
    <div style={{ display: 'flex', gap: '12px', alignItems: 'stretch', width: '100%' }}>
      <div id="category-dropdown-container" style={{ position: 'relative', display: 'inline-block', flex: 1, minWidth: 0 }}>
        <button
          id="dropdown-trigger"
          type="button"
          style={{
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
      width: '100%',
      padding: '6px 12px',
      borderRadius: '8px',
      border: '1px solid var(--cat-dropdown-border)',
      backgroundColor: 'var(--cat-dropdown-bg)',
      color: 'var(--cat-dropdown-text)',
      fontSize: '14px',
      fontWeight: '500',
      cursor: 'pointer',
      textAlign: 'left',
      boxShadow: '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
      minHeight: '42px',
      gap: '12px'
    }}
        >
          <div id="dropdown-trigger-content" style={{ display: 'flex', flexWrap: 'wrap', gap: '6px', alignItems: 'center', flex: 1, minWidth: 0 }}>
            <span id="dropdown-trigger-placeholder" style={{ color: '#64748b' }}>Filter by category...</span>
          </div>

          <svg style={{ width: '16px', height: '16px', color: '#64748b', flexShrink: 0 }} fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 9l-7 7-7-7" />
          </svg>
        </button>

        <div
          id="dropdown-menu"
          style={{
      display: 'none',
      position: 'absolute',
      top: '100%',
      left: '0',
      right: '0',
      marginTop: '6px',
      padding: '8px',
      borderRadius: '8px',
      border: '1px solid var(--cat-dropdown-border)',
      backgroundColor: 'var(--cat-dropdown-bg)',
      color: 'var(--cat-dropdown-text)',
      zIndex: 100,
      maxHeight: '280px',
      overflowY: 'auto',
      boxShadow: '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)'
    }}
        >
          <div id="category-options-list" style={{ display: 'flex', flexDirection: 'column', gap: '2px' }} />
        </div>
      </div>

      <button
        id="native-filter-toggle"
        type="button"
        aria-pressed="false"
        style={{
    display: 'flex',
    alignItems: 'center',
    gap: '6px',
    padding: '6px 16px',
    borderRadius: '8px',
    border: '1px solid var(--cat-dropdown-border)',
    backgroundColor: 'var(--cat-dropdown-bg)',
    color: 'var(--cat-dropdown-text)',
    fontSize: '14px',
    fontWeight: '600',
    cursor: 'pointer',
    whiteSpace: 'nowrap',
    boxShadow: '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
    minHeight: '42px'
  }}
      >
        Native only
      </button>
    </div>
  </div>

  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '16px' }} id="integrations-grid" />

  <div id="pagination-controls" style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '8px', marginTop: '32px', marginBottom: '16px' }} />

  <div id="no-results" style={{ display: 'none', textAlign: 'center', padding: '40px', color: '#64748b' }}>
    <p style={{ fontSize: '16px', margin: 0 }}>No integrations found matching your search.</p>
    <p style={{ fontSize: '14px', marginTop: '4px' }}>But don't worry! Any external service with an API can be connected via Pipedream MCP.</p>
  </div>
</div>

<script src="/scripts/integrations_data.js" defer />

<script src="/scripts/integrations-catalog.js" defer />


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.