<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    
    <xsl:template match="/">
    
    <html>
        <body>
            
            <h2>Pokédex</h2>

            <div>
                <div>
                    <table>
                        <xsl:for-each select= "pokedex/pokemon">
                            <tr>
                                <td>
                                    <xsl:value-of select="@num_pokedex"/>
                                </td>
                                <td>
                                    <xsl:value-of select="@nombre"/>
                                </td>
                            </tr>
                            <tr>
                                <xsl:value-of select = "imagen"/>
                            </tr>
                        </xsl:for-each>
                    </table>
                </div>

                <div>
                
                </div>

                <div>
                
                </div>
            </div>
        </body>
    </html>

    </xsl:template>

</xsl:stylesheet>