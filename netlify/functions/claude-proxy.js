const https = require('https');

exports.handler = async function(event) {
  const allowedOrigins = [
    'https://www.musicproductionwiki.com',
    'https://musicproductionwiki.com'
  ];
  const origin = event.headers && (event.headers.origin || event.headers.Origin);
  const corsOrigin = allowedOrigins.includes(origin) ? origin : allowedOrigins[0];

  const corsHeaders = {
    'Access-Control-Allow-Origin': corsOrigin,
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Content-Type': 'application/json'
  };

  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 200, headers: corsHeaders, body: '' };
  }

  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, headers: corsHeaders, body: JSON.stringify({ error: 'Method not allowed' }) };
  }

  const ANTHROPIC_API_KEY = process.env.ANTHROPIC_API_KEY;
  if (!ANTHROPIC_API_KEY) {
    return { statusCode: 500, headers: corsHeaders, body: JSON.stringify({ error: 'API key not configured' }) };
  }

  return new Promise((resolve) => {
    try {
      const bodyStr = JSON.stringify(JSON.parse(event.body));
      const options = {
        hostname: 'api.anthropic.com',
        path: '/v1/messages',
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Content-Length': Buffer.byteLength(bodyStr),
          'x-api-key': ANTHROPIC_API_KEY,
          'anthropic-version': '2023-06-01'
        }
      };

      const req = https.request(options, (res) => {
        let data = '';
        res.on('data', (chunk) => { data += chunk; });
        res.on('end', () => {
          resolve({
            statusCode: res.statusCode,
            headers: corsHeaders,
            body: data
          });
        });
      });

      req.on('error', (err) => {
        resolve({
          statusCode: 500,
          headers: corsHeaders,
          body: JSON.stringify({ error: err.message })
        });
      });

      req.write(bodyStr);
      req.end();

    } catch (err) {
      resolve({
        statusCode: 500,
        headers: corsHeaders,
        body: JSON.stringify({ error: err.message })
      });
    }
  });
};
